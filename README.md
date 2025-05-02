# Form Data Recovery with Memento Pattern

This repository contains a simple implementation of the **Memento Design Pattern** to demonstrate **Form Data Recovery** in a web application. The idea is to store the state of a form, so that if a user navigates away accidentally, they can restore their previous entries.

## Project Overview

In many web applications, forms are an integral part of user interactions. Sometimes, users may lose their form data due to accidental navigation. This implementation of the **Memento Pattern** allows for storing and restoring form data to avoid such issues.

### Design Pattern Used: Memento

- **Memento**: Captures and stores the current state of an object (in this case, the form).
- **Caretaker**: Manages the mementos and provides the ability to restore the form data.
- **Originator**: The object (form) whose state is being saved or restored.

## Features

- Save the current form state (data).
- Restore the form state to a previously saved state.
- Supports simple form data such as name and email.
