<template>
  <div class="fr-container--fluid">
    
    <div style="width: 80%; margin: auto; margin-top: 50px;">
    Indiquez votre cohorte (séparé pour une virgule)
    <input class="fr-input" v-model="currentCohorte">
    <br />
    Période (optionnel)
    <div style="display: flex">
      <input style="width: 200px" class="fr-input" v-model="currentMinPeriode">&nbsp;&nbsp;&nbsp;à&nbsp;&nbsp;&nbsp;<input style="width: 200px" class="fr-input" v-model="currentMaxPeriode">
    </div>

    <button style="margin-top: 10px;" class="fr-btn" @click="queryApi()">Rechercher</button>&nbsp;&nbsp;
    <button style="margin-top: 10px;" class="fr-btn" @click="demook()">Démo OK</button>&nbsp;&nbsp;
    <button style="margin-top: 10px;" class="fr-btn" @click="demoko()">Démo KO</button>

    </div>
    <div v-if="firstSearch">
    <div v-if="showGraph" style="width: 80%; margin: auto; margin-top: 50px;">
      <div v-if="x.length > 0">
        <bar-or-graph indicateur="toto" color="#3558a2" titleChart="Retour à l'emploi d'après une cohorte" unitChart="%" typeChart="bar" :valuesx="x" :valuesy="y"></bar-or-graph>

        Cohorte : {{ cohorte }} personnes
      </div>
    </div>

    <div v-if="!showGraph" style="width: 80%; margin: auto; margin-top: 50px;">
        Votre cohorte doit comporter au minimum 20 personnes.
    </div>
    <br />
    </div>
  </div>
</template>

<script>
import BarOrGraph from '@/components/BarOrGraph.vue'

export default {
  name: 'AppIAE',
  components: {BarOrGraph},
  metaInfo: {
    title: "Tableau de bord IAE",
    meta: [
      {
        name: "description",
        content: "description.",
      },
      // Ajoutez d'autres balises meta si nécessaire
    ],
  },
  data() {
    return {
      currentCohorte: null,
      m1: null,
      m3: null,
      m6: null,
      m9: null,
      m12: null,
      cohorte: null,
      currentMinPeriode: null,
      currentMaxPeriode: null,
      x: [],
      y: [],
      showGraph: false,
      firstSearch: false,
    }
  },
  computed: {
  },
  mounted() {
  },
  methods: {
    demook(){
        this.currentCohorte = "" // set up 100 id_assures
        this.queryApi()
    },
    demoko(){
        this.currentCohorte = "" // set up < 20 assures
        this.queryApi()
    },
    queryApi(){
      this.firstSearch = true
      if (this.currentCohorte.split(",").length > 20) {
        this.showGraph = true
        let arr = []
        if(this.currentCohorte){
            arr.push("cohorte=" + this.currentCohorte)
        }
        if(this.currentMinPeriode){
            arr.push("min_fin_accompagnement=" + this.currentMinPeriode)
        }
        if(this.currentMaxPeriode){
            arr.push("max_fin_accompagnement=" + this.currentMaxPeriode)
        }
        let str = "?" + arr.join('&')

        fetch("http://10.0.0.55:3030/get_cohorte" + str)
            .then((response) => {
                return response.json()
            })
            .then((data) => {
            console.log(data)
            this.m1 = data.m1
            this.m3 = data.m3
            this.m6 = data.m6
            this.m9 = data.m9
            this.m12 = data.m12
            this.x = ["m1", "m3", "m6", "m9", "m12"]
            this.y = [this.m1, this.m3, this.m6, this.m9, this.m12]
            this.cohorte = data.nb
            });
      } else {
        this.showGraph = false

      }
    }
  },
  watch: {
  }
}
</script>

<style scoped>
.bloc-select{
  max-width: 200px;
  max-height: 200px;
  border: 1px solid red;
  padding: 20px;
  margin-right: 20px;
}

.bloc-input{
  max-width: 400px;
  max-height: 200px;
  border: 1px solid red;
  padding: 20px;
  margin-right: 20px;
}

.selects{
  display: flex;
}
</style>