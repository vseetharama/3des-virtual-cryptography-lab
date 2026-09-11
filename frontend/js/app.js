import { runOperation } from './api.js';
import { renderPipeline, renderResult } from './visualizer.js?v=3';

const form = document.querySelector('#operation-form');
const plaintext = document.querySelector('#plaintext');
const ciphertext = document.querySelector('#ciphertext');
const message = document.querySelector('#message');
const pipeline = document.querySelector('#pipeline');
const result = document.querySelector('#result-content');
const resultStatus = document.querySelector('#result-status');
const submitButton = document.querySelector('#submit-button');
let mode = 'encrypt';
const DEMO_KEY_HEX = '133457799bbcdff11234567890abcdef23456789abcdef01';

function setMode(nextMode) { mode = nextMode; document.querySelector('#plaintext-field').classList.toggle('hidden', mode !== 'encrypt'); document.querySelector('#ciphertext-field').classList.toggle('hidden', mode !== 'decrypt'); submitButton.textContent = mode === 'encrypt' ? 'Run encryption' : 'Run decryption'; document.querySelectorAll('.mode-button').forEach(button => { const active = button.dataset.mode === mode; button.classList.toggle('active', active); button.setAttribute('aria-selected', active); }); message.textContent = ''; }
function validate() { if (mode === 'encrypt' && !plaintext.value) return 'Plaintext must not be empty.'; if (mode === 'decrypt' && (!/^[0-9a-fA-F]+$/.test(ciphertext.value) || ciphertext.value.length % 16 !== 0)) return 'Ciphertext must be hexadecimal and aligned to 8-byte blocks.'; return ''; }
document.querySelectorAll('.mode-button').forEach(button => button.addEventListener('click', () => setMode(button.dataset.mode)));
document.querySelector('#reset-button').addEventListener('click', () => { form.reset(); setMode('encrypt'); pipeline.innerHTML = '<div class="empty-pipeline"><span class="empty-number">00</span><p>Enter your message or ciphertext, then run an operation to reveal the transformation.</p></div>'; result.innerHTML = '<p class="muted">Intermediate values and verification will appear here after a successful operation.</p>'; resultStatus.textContent = 'Awaiting operation'; });
form.addEventListener('submit', async event => { event.preventDefault(); message.textContent = validate(); if (message.textContent) return; submitButton.disabled = true; submitButton.textContent = 'Processing 3DES...'; resultStatus.textContent = 'Processing'; try { const response = await runOperation(mode, mode === 'encrypt' ? { plaintext: plaintext.value, key_hex: DEMO_KEY_HEX } : { ciphertext_hex: ciphertext.value, key_hex: DEMO_KEY_HEX }); renderPipeline(pipeline, response); renderResult(result, response, plaintext.value); resultStatus.textContent = 'Complete'; if (mode === 'encrypt') ciphertext.value = response.ciphertext_hex; } catch (error) { message.textContent = error.message; resultStatus.textContent = 'Input error'; } finally { submitButton.disabled = false; submitButton.textContent = mode === 'encrypt' ? 'Run encryption' : 'Run decryption'; } });