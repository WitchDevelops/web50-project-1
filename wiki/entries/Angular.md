# Angular

Angular is a **TypeScript-based web framework** developed by Google for building dynamic, single-page applications (SPAs). It provides a **component-based architecture**, built-in tools for state management, and a powerful dependency injection system.

## Key Features
- **Component-Based**: Applications are built using modular and reusable components.
- **Two-Way Data Binding**: Synchronizes data between the model and the view automatically.
- **Dependency Injection**: Efficiently manages services and dependencies.
- **Routing and State Management**: Provides built-in navigation and state management tools.
- **Reactive Programming**: Uses RxJS for handling asynchronous operations.

## Example Code (Component)

```
import { Component } from '@angular/core';
@Component({
  selector: 'app-hello',
  template: `<h1>Hello, {{ name }}!</h1>`,
})
export class HelloComponent {
  name: string = 'Angular';
}
```

Angular is widely used for enterprise applications due to its scalability and structured architecture.