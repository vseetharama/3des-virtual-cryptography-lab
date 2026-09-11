const labels = { DES_ENCRYPT: 'Encrypt', DES_DECRYPT: 'Decrypt' };

export function renderPipeline(container, response) {
  const inputLabel = response.operation === 'encrypt' ? 'Plaintext → UTF-8 bytes' : 'Ciphertext';
  const paddingNode = response.operation === 'encrypt' ? '<div class="stage-node"><div class="stage-title">PKCS#7 Padding</div><div class="stage-meta">DES block size: 8 bytes (64 bits)</div></div>' : '';
  const unpaddingNode = response.operation === 'decrypt' ? '<div class="stage-node"><div class="stage-title">Remove PKCS#7 Padding</div><div class="stage-meta">Validate and remove padding bytes</div></div>' : '';
  const finalLabel = response.operation === 'encrypt' ? 'Ciphertext' : 'Plaintext';
  const ciphertextBytes = response.operation === 'encrypt' ? response.ciphertext_hex.length / 2 : 0;
  const ciphertextBlocks = ciphertextBytes / 8;
  const finalMeta = response.operation === 'encrypt' ? `${ciphertextBytes} bytes (${ciphertextBlocks} × 64-bit blocks)` : 'UTF-8 decoded';
  container.innerHTML = `<div class="stage-node"><div class="stage-title">Input</div><div class="stage-meta">${inputLabel}</div></div>${paddingNode}${response.stages.map((stage, index) => `<div class="stage-node ${index === 0 ? 'active' : ''}"><div class="stage-title">Stage ${stage.stage}: DES ${labels[stage.operation]} ${stage.key}</div><div class="stage-meta">${stage.input_hex.length / 2} bytes in → ${stage.output_hex.length / 2} bytes out</div></div>`).join('')}${unpaddingNode}<div class="stage-node"><div class="stage-title">${finalLabel}</div><div class="stage-meta">${finalMeta}</div></div>`;
}

export function renderResult(container, response, originalPlaintext) {
  const stageCells = response.stages.map(stage => `<div class="result-cell"><strong>Stage ${stage.stage} · ${stage.operation} ${stage.key}</strong><div class="hex">${stage.output_hex}</div></div>`).join('');
  const final = response.operation === 'encrypt' ? `<div class="result-cell"><strong>Ciphertext</strong><div class="hex">${response.ciphertext_hex}</div></div>` : `<div class="result-cell"><strong>Recovered plaintext</strong><div>${escapeHtml(response.plaintext)}</div></div><div class="verification"><strong>Verification: ${response.plaintext === originalPlaintext ? 'SUCCESS' : 'FAILED'}</strong><br>Recovered text ${response.plaintext === originalPlaintext ? 'matches' : 'does not match'} the original input.</div>`;
  container.innerHTML = `<div class="result-grid">${final}${stageCells}</div>`;
}

function escapeHtml(value) { return value.replace(/[&<>'"]/g, character => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' }[character])); }