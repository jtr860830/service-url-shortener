const Router = require("koa-router");
const Bodyparser = require("koa-bodyparser");
const Logger = require("koa-logger");

const models = require("../models");

const router = new Router();

router.use(Bodyparser());
router.use(Logger());

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