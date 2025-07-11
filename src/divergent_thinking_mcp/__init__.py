"""
Divergent Thinking MCP Server

A Model Context Protocol server that promotes absurd, non-linear, and creative
thinking patterns for artistic creation - the opposite of sequential logical thinking.

Features interactive domain specification with 78+ multi-word domains for targeted
creativity, comprehensive context parameters (audience, time, resources, goals),
and 6 proven creativity methodologies through a unified interface.
"""

__version__ = "0.2.1"
__author__ = "Fridayxiao"

from .divergent_mcp import app, main

__all__ = ["app", "main"]