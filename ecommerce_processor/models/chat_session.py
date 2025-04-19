from dataclasses import dataclass, field

"""
This module defines the Transaction class, which represents a transaction with various attributes.
"""
@dataclass
class ChatSession:
    session_id: str
    source: str
    messages: list = field(default_factory=list)  # Use default_factory for mutable types
    html_content: str = None
    prompt: str = None

    @staticmethod
    def to_user_dict(session: 'ChatSession') -> dict:
        """
        Converts a ChatSession instance to a dictionary.
        """
        return {
            'session_id': session.session_id,
            'source': session.source,
            'messages': session.messages
        }