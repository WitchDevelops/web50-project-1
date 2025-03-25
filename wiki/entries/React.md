# React

React is a popular [JavaScript](/wiki/JavaScript) library for building interactive user interfaces, particularly for **single-page applications (SPAs)**. Developed by Facebook, it allows developers to create reusable UI components and efficiently update the DOM using a virtual DOM.

## Key Features
- **Component-Based**: UI is built using reusable components.
- **Virtual DOM**: Enhances performance by minimizing direct DOM updates.
- **State Management**: Uses `useState` and `useEffect` hooks for handling state in functional components.
- **[JSX Syntax](/wiki/JSX)**: Combines JavaScript and HTML-like syntax for cleaner code.

## Example Code

```
import React, { useState } from "react";
function Counter() {
    const [count, setCount] = useState(0);   
    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={() => setCount(count + 1)}>Increment</button>
        </div>
    );
}
export default Counter;
```


React is widely used in modern web development, with frameworks like Next.js enhancing its capabilities for server-side rendering and static site generation.