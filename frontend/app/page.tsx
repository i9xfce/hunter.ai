const stats = [
  ['Total de vagas', '1.258'],
  ['Aplicadas', '845'],
  ['Pendentes', '22'],
  ['Entrevistas', '18'],
  ['Match médio', '91%'],
]

export default function Home() {
  return (
    <main className="min-h-screen bg-slate-950 p-8 text-white">
      <section className="mx-auto max-w-6xl">
        <p className="text-sm uppercase tracking-widest text-cyan-300">JobHunter AI</p>
        <h1 className="mt-3 text-4xl font-bold">AI Job Agent para vagas de Tecnologia</h1>
        <p className="mt-4 max-w-3xl text-slate-300">
          Busque vagas, calcule aderência, gere materiais personalizados e acompanhe candidaturas com confirmação humana antes de qualquer envio sensível.
        </p>
        <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-5">
          {stats.map(([label, value]) => (
            <article key={label} className="rounded-2xl border border-slate-800 bg-slate-900 p-5">
              <p className="text-sm text-slate-400">{label}</p>
              <strong className="mt-2 block text-3xl">{value}</strong>
            </article>
          ))}
        </div>
      </section>
    </main>
  )
}
