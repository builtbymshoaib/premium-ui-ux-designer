export function FAQ({ items }: { items: { id: string; question: string; answer: string }[] }) {
  return <div className="ui-faq">{items.map(item => <details key={item.id}><summary>{item.question}</summary><p>{item.answer}</p></details>)}</div>;
}
