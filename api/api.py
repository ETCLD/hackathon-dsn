from aiohttp import web, ClientSession
import aiohttp_cors
from markupsafe import escape
import json
import pandas as pd

df = pd.read_csv("kpis_10_21.csv", dtype={
    "id_assure": str,
    "complement_dispositif_public": str, "fin_accompagnement": str, "sexe": str, "dep_et_m1": str,
    "dep_et_m3": str, "dep_et_m6": str, "dep_et_m9": str, "dep_et_m12": str, "cj_et_m1": str, "cj_et_m3": str, "cj_et_m6": str, "cj_et_m9": str, "cj_et_m12": str,
    "nature_contrat_m1": str, "nature_contrat_m3": str, "nature_contrat_m6": str, "nature_contrat_m9": str, "nature_contrat_m12": str,
    "et_ad_code_postal": str
})
df["contrat_m1"] = df["contrat_m1"].astype(bool)
df["contrat_m3"] = df["contrat_m3"].astype(bool)
df["contrat_m6"] = df["contrat_m6"].astype(bool)
df["contrat_m9"] = df["contrat_m9"].astype(bool)
df["contrat_m12"] = df["contrat_m12"].astype(bool)
df.age = df.age.astype(float)

routes = web.RouteTableDef()


def get_months(dfinter):
    if dfinter.shape[0] > 0:
        mydict = {}
        for month in ["m1", "m3", "m6", "m9", "m12"]:
            taux = round(((
                dfinter[dfinter["contrat_" + month] == True].shape[0] / (
                    dfinter[dfinter["contrat_" + month] == True].shape[0] + dfinter[dfinter["contrat_" + month] == False].shape[0]
                )
            ) * 100), 2)
            mydict[month] = taux
        mydict["nb"] = dfinter.shape[0]
        return mydict
    else:
        return {"m1": None, "m2": None, "m3": None, "m9": None, "m12": None, "nb": 0}
        

@routes.get("/")
async def get_health(request):
    return web.HTTPOk()


@routes.get('/get_kpi')
async def get_kpi(request):
    dfinter = df
    if "min_fin_accompagnement" in request.rel_url.query:
        dfinter = dfinter[dfinter["fin_accompagnement"] >= request.rel_url.query['min_fin_accompagnement']]
    if "max_fin_accompagnement" in request.rel_url.query:
        dfinter = dfinter[dfinter["fin_accompagnement"] <= request.rel_url.query['max_fin_accompagnement']]
    if "complement_dispositif_public" in request.rel_url.query:
        dfinter = dfinter[dfinter["complement_dispositif_public"] == request.rel_url.query['complement_dispositif_public']]
    if "sexe" in request.rel_url.query:
        dfinter = dfinter[dfinter["sexe"] == request.rel_url.query['sexe']]
    if "dep" in request.rel_url.query:
        dfinter = dfinter[dfinter["et_ad_code_postal"] == request.rel_url.query['dep']]
    if "min_age" in request.rel_url.query:
        dfinter = dfinter[dfinter["age"] >= int(request.rel_url.query['min_age'])]
    if "max_age" in request.rel_url.query:
        dfinter = dfinter[dfinter["age"] <= int(request.rel_url.query['max_age'])]
    return web.json_response(text=json.dumps(get_months(dfinter), default=str))


@routes.get('/get_cohorte')
async def get_kpi(request):
    dfinter = df
    if "cohorte" in request.rel_url.query:
        cohorte = request.rel_url.query["cohorte"].split(",")
        print(cohorte)
        dfinter = dfinter[dfinter["id_assure"].isin(cohorte)]
        print(dfinter.shape)
    if "min_fin_accompagnement" in request.rel_url.query:
        dfinter = dfinter[dfinter["fin_accompagnement"] >= request.rel_url.query['min_fin_accompagnement']]
    if "max_fin_accompagnement" in request.rel_url.query:
        dfinter = dfinter[dfinter["fin_accompagnement"] <= request.rel_url.query['max_fin_accompagnement']]
    return web.json_response(text=json.dumps(get_months(dfinter), default=str))


async def app_factory():
    async def on_startup(app):
        app["csession"] = ClientSession()

    async def on_cleanup(app):
        await app["csession"].close()

    app = web.Application()
    app.add_routes(routes)
    app.on_startup.append(on_startup)
    app.on_cleanup.append(on_cleanup)

    cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*"
        )
    })

    for route in list(app.router.routes()):
        cors.add(route)
        
    return app


def run():
    web.run_app(app_factory(), path="0.0.0.0", port="3030")


if __name__ == "__main__":
    run()