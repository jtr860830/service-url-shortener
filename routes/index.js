const Router = require("@koa/router");
const CORS = require("@koa/cors");
const Logger = require("koa-logger");
const Bodyparser = require("koa-bodyparser");

const models = require("../models");

const router = new Router();

router.use(CORS());
router.use(Logger());
router.use(Bodyparser());

router.post("/short", async (ctx) => {
	try {
		const url = await models.URL.create({ real: ctx.request.body.url });
		ctx.response.status = 201;
		ctx.response.body = { data: url };
	} catch (err) {
		console.error(err);
		ctx.response.status = 500;
	}
});

router.get("/:alias", async (ctx) => {
	try {
		const url = await models.URL.findOne({ alias: ctx.params.alias });
		if (url == null) ctx.response.status = 404;
		else ctx.redirect(url.real);
	} catch (err) {
		console.error(err);
		ctx.response.status = 500;
	}
});