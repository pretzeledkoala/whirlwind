[![Whirlwind](image.png)](https://pretzeledkoala.vercel.app/blog/cs.se/whirlwind)

# What is Whirlwind?

Whirlwind is a workstation for scribing lightning-fast in-class LaTeX notes. It's designed to be simple, fast, and versatile.

# Goals

The goals of whirlwind are threefold:

- **Simplicity**. Experience all of your favorite LaTeX features in a streamlined markdown environment. Enjoy a tiny learning curve with minimal debugging hassles. Effortlessly maintain an organized folder structure.
- **Speed**. Use dozens of predefined code snippets for rapid note-taking. Set up within seconds, write effortlessly, and update with unparalleled speed.
- **Versatility**. Export notes directly to the web or convert them into raw LaTeX files effortlessly. Tailor your note-taking experience with highly customizable settings. Collaborate seamlessly with your favorite friends.

# Getting started 

1. Clone the [github codebase](https://github.com/pretzeledkoala/whirlwind) locally: `git clone https://github.com/pretzeledkoala/whirlwind`
2. Set up the snippets file: `Open command palette (⌘P)` $\to$ `Snippets: configure user snippets` $\to$ `new snippets file` (both local and global work) $\to$ copy and paste `/.vscode/snippets.json` into this file.
3. Open `notes/template.md`, the markdown preview for the markdown file (`⌘K V`), and start taking notes!

# Features 
- Popular LaTeX theorem and proof environments, but CSS'ed
- 38 LaTeX snippets to help you type faster
- 31 folders in `/notes` to categorize your notes, following the [arXiv math classification](https://arxiv.org/archive/math)
- Run `./links.sh` to see 12 other useful math tools on the web
- Ability to port to the web via [quartz](https://quartz.jzhao.xyz/) or the [tailwind next.js starter blog](https://github.com/timlrx/tailwind-nextjs-starter-blog).

# Coming Soon 
- <ins>Website</ins>: Allows for more rapid user onboarding without the need for a local set up.
- <ins>Bibliography Management</ins>: Tools for managing citations and bibliographies quickly, making it easier to reference sources and create well-documented notes.
- <ins>Customizable Themes</ins>: User designed themes to provide a personalized and visually appealing note-taking experience.
- <ins>Enhanced Export Options</ins>: Export directly to HTML and other requested formats.
- <ins>Image Integration</ins>: Novel optimizations for drawing and inserting diagrams in-class.
- <ins>More Snippets</ins>: Feel free to suggest your own!

If any of this sounds interesting to you, submit your own features, reach out to [garyhu06@gmail.com](mailto:garyhu06@gmail.com), and/or join the [email list](https://forms.gle/4QoSZUoLCcGP1M7VA).

# Acknowledgements 

Built for [n&w s5](https://buildspace.so/).