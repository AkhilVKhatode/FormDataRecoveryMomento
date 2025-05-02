class FormMemento:
    """Memento that stores the state of the form."""
    def __init__(self, data):
        self._data = data
    
    def get_data(self):
        return self._data


class Form:
    """Form that has data (fields) and allows saving/restoring states."""
    def __init__(self):
        self._data = {}
    
    def set_data(self, field, value):
        """Set data for a specific field in the form."""
        self._data[field] = value
    
    def get_data(self):
        """Get the current form data."""
        return self._data
    
    def create_memento(self):
        """Create a memento to save the current state."""
        return FormMemento(self._data.copy())
    
    def restore_memento(self, memento):
        """Restore the form state from a memento."""
        self._data = memento.get_data()


class FormDataCaretaker:
    """Caretaker that stores and retrieves the form state."""
    def __init__(self):
        self._mementos = []
    
    def save(self, memento):
        """Save a memento."""
        self._mementos.append(memento)
    
    def restore(self):
        """Restore the most recent memento."""
        if self._mementos:
            return self._mementos.pop()
        return None


# Example usage

# Create a form instance
form = Form()

# User fills in some fields
form.set_data("name", "John Doe")
form.set_data("email", "johndoe@example.com")

# Caretaker to save and restore form data
caretaker = FormDataCaretaker()

# Save the current state
caretaker.save(form.create_memento())

# Simulate user making changes to the form
form.set_data("name", "Jane Smith")
form.set_data("email", "janesmith@example.com")

# Print updated data
print("Updated form data:", form.get_data())

# Restore the previous state
memento = caretaker.restore()
if memento:
    form.restore_memento(memento)
    print("Restored form data:", form.get_data())
