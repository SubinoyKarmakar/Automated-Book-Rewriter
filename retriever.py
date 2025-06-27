memory = {}     # In-memory dictionary to temporarily store document versions

def store_in_memory(doc_id, content, metadata):     # Save content and its metadata in memory under a unique document ID.
    memory[doc_id] = {
        "content": content,
        "metadata": metadata
    }

def retrieve_from_memory(doc_id):       # Retrieve stored content and metadata using the document ID.
    return memory.get(doc_id, None)     # Returns None if not found.