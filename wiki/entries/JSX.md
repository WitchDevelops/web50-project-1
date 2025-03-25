# JSX

JSX (JavaScript XML) is a syntax extension for [JavaScript](/wiki/JavaScript) used in [React](/wiki/React) to define UI components in a way that resembles HTML. It makes it easier to write and visualize component structures while integrating JavaScript logic.

## Key Features
- **HTML-like Syntax**: JSX allows writing UI elements in JavaScript.
- **JavaScript Integration**: You can embed JavaScript expressions using `{}`.
- **Babel Compilation**: JSX is not native to browsers and gets transpiled into regular JavaScript by tools like Babel.

## Example Code
```
const element = <h1>Hello, World!</h1>;
```
This compiles to:
```
const element = React.createElement("h1", null, "Hello, World!");
```
JSX improves readability and maintainability, making [React](/wiki/React) development more intuitive.