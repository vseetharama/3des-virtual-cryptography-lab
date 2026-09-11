export async function runOperation(mode, payload) {
  const response = await fetch(`/api/v1/${mode}`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
  const body = await response.json();
  if (!response.ok) throw new Error(body.detail?.message || body.error?.message || 'The operation could not be completed.');
  return body;
}