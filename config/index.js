const _ = require("lodash");

const env = process.env.NODE_ENV;
const port = +process.env.PORT || 8080;
const host = process.env.HOST || "0.0.0.0";
const db = {
	url: process.env.MONGO_URL || "mongodb://127.0.0.1:27017/",
	dbname: process.env.MONGO_DB || "url_shortener"
};

const config = {
	env,
	port,
	host,
	db
};

try {
	_.merge(config, require("./" + env));
} catch (err) {
	console.error(err);
}

module.exports = config;