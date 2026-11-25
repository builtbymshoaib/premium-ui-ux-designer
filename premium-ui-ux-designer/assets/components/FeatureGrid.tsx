export function FeatureGrid({ items }: { items: { id: string; title: string; description: string }[] }) {
  return <ul className="ui-grid" style={{listStyle:"none",padding:0}}>{items.map(item => <li key={item.id}><h3>{item.title}</h3><p>{item.description}</p></li>)}</ul>;
}
