const Koa = require("koa");
const routes = require("./routes");
const config = require("./config");

const app = Koa();
app.use(routes);

app.listen(config.port, config.host);