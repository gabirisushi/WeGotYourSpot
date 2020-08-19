/*
const api = path => `http://localhost:9090/api/customer-analyse/${path}`;
class Network {
  constructor(){
    this.URL_PRODUCT_LIST = api("statistic");
    this.URL_PRODUCT_ANALYSIS = api("analysis");
    const Promise = this.Promise || require("promise");
    this.agentDefault = require("superagent-promise")(require("superagent"), Promise);
  }
  // network call to get statistic
  doGetStatistic() {
    return this.agentDefault("GET", this.URL_PRODUCT_LIST).end();
  }
  //network call to get analysis
  doGetProduct(id) {
    return this.agentDefault("GET", this.URL_PRODUCT_ANALYSIS+"/"+id);
  }
}

export default new Network();
*/
