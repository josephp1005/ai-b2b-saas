import express from 'express';
import morgan from 'morgan';

const app = express();
app.use(express.json());
app.use(morgan('dev'));

app.get('/health', (_req, res) => {
  console.log('[node-api] /health ping');
  res.json({ ok: true, service: 'node-api' });
});

app.get('/wallet/:address', (req, res) => {
  const { address } = req.params;
  console.log('[node-api] GET /wallet', { address });
  res.json({ address, balance: '0', note: 'placeholder' });
});

app.post('/tx/simulate', (req, res) => {
  console.log('[node-api] POST /tx/simulate body=', req.body);
  res.json({ simulated: true, echo: req.body });
});

const port = process.env.PORT || 3001;
app.listen(port, () => console.log(`node-api listening on :${port}`));