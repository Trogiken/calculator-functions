// dyn-nav.js

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('shared-nav-container').innerHTML = `
        <nav class="sidebar">
            <h2>Docs Pages</h2>
            <ul>
                <li><a href="introduction.html">Introduction</a></li>
                <li><a href="installation.html">Installation</a></li>
                <li><a href="usage.html">Usage</a></li>
                <li><a href="examples.html">Examples</a></li>
                <li><a href="api-reference.html">API Reference</a></li>
                <li><a href="faq.html">FAQ</a></li>
                <li><a href="contributing.html">Contributing</a></li>
            </ul>
        </nav>
    `;
});
