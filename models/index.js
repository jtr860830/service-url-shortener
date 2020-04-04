const mongoose = require("mongoose");
const config = require("../config");
const URL = require("./url.js");

mongoose.connect(config.db.url + config.db.dbname, {useNewUrlParser: true});
mongoose.connection.on("error", console.error.bind(console, "connection error:"));

const models = {
	URL
};

module.exports = models;