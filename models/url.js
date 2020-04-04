const mongoose = require("mongoose");
const shorID = require("shortid");

const URL = mongoose.Schema({
	real: {
		type: String,
		required: true
	},
	ailas: {
		type: String,
		required: true,
		default: shorID.generate
	},
	clicks: {
		type: Number,
		required: true,
		default: 0
	}
});

module.exports = mongoose.model("url", URL);