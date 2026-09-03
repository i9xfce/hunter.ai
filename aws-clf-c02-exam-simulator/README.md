# AWS Cloud Practitioner Exam Simulator (CLF-C02)

Simulador educacional em português para preparação da certificação AWS Certified Cloud Practitioner. A interface usa um tema inspirado na AWS e oferece estudo guiado e prova cronometrada.

## Recursos

- **Official Exam Mode**: 65 posições, 90 minutos e a distribuição 24/30/34/12 do blueprint (16/20/22/7).
- **Modo estudo**: feedback instantâneo e explicações por questão.
- Banco JSON local com **50 questões realistas de validação**, tipadas e organizadas para expansão a 300+ sem alterar componentes.
- Monitoramento de foco com Visibility API, blur, `beforeunload` e detecção de saída do fullscreen; alerta acessível e sirene Web Audio.
- Relatório com nota estimada, acertos por domínio, infrações, certificado simbólico a partir de 700 e exportação JSON/PDF (impressão).
- API Express endurecida com Helmet/CSP, CORS restrito, rate limiting, validação Zod e SQLite.

> Limite importante: APIs do navegador são mecanismos de dissuasão, não uma solução antifraude. Elas não detectam outro dispositivo, captura de tela ou todos os tipos de minimização. Não use este projeto para avaliação de alto risco.

## Executar

```bash
npm install
npm run dev
```

Abra `http://localhost:5173`. O Vite inicia o frontend e a API fica em `http://localhost:3001`. Para produção:

```bash
npm run build
npm run start
```

## Estrutura

```text
src/data/questions.ts       Banco JSON/TypeScript inicial e blueprint
src/pages                  Landing, prova e relatório
src/components             Questão, cronômetro e alerta de proctoring
src/hooks/useProctoring.ts Monitoramento de browser encapsulado
server/index.ts             API Express e persistência SQLite
```

## Arquitetura e expansão

O frontend mantém respostas no estado da sessão e a API aceita tentativas validadas em `POST /api/attempts`. Para chegar a 300+ questões, importe registros com o mesmo contrato de `Question`, mantenha alternativas A–D e adicione questões por domínio respeitando `targetDistribution`. Em produção, mova autenticação e progresso para uma identidade de usuário, use banco gerenciado, auditoria e uma fila para analytics. Nunca confie em score calculado no cliente para certificação real.

## Segurança e acessibilidade

Entradas da API passam por schema Zod e são serializadas pelo React, evitando renderização HTML arbitrária. Helmet define CSP; payloads são limitados e o endpoint tem limitação de taxa. Os controles possuem foco visível, labels e `role=alertdialog`. Antes de uma implantação pública, adicione autenticação, CSRF conforme estratégia de cookie, observabilidade, testes E2E, revisão de dependências e uma política de privacidade.

## Próximas melhorias

- Substituir o banco inicial por 300+ perguntas revisadas por SMEs.
- Adicionar favoritos, flashcards persistentes e dashboard histórico autenticado.
- Adicionar gráficos radar/barras com uma biblioteca de visualização e testes automatizados.
- Implementar geração de PDF no servidor e internacionalização completa.

## Deploy no GitHub Pages

O workflow [`../.github/workflows/deploy-aws-clf-c02.yml`](../.github/workflows/deploy-aws-clf-c02.yml) constrói e publica o **frontend estático** em GitHub Pages quando alterações deste diretório chegam a `main` ou `master`. Antes do primeiro deploy, habilite **Settings → Pages → Source: GitHub Actions** no repositório `denisribalves/awscf-02-certification`.

O Express/SQLite é uma API Node separada e não é executado pelo GitHub Pages. Para usar persistência em produção, faça o deploy do conteúdo de `server/` em um host Node compatível e configure `CORS_ORIGIN` com a URL publicada do Pages.
