#!/usr/bin/env python3
"""
Search Hyprland documentation and configuration variables.

This script fetches and searches the Hyprland wiki for configuration
variables, keybindings, and documentation.
"""

import sys
import re
import json
from typing import List, Dict
import urllib.request
import urllib.error

# Hyprland wiki URLs
WIKI_URLS = {
    "variables": "https://wiki.hyprland.org/Configuring/Variables/",
    "keywords": "https://wiki.hyprland.org/Configuring/Keywords/",
    "binds": "https://wiki.hyprland.org/Configuring/Binds/",
    "animations": "https://wiki.hyprland.org/Configuring/Animations/",
    "dispatchers": "https://wiki.hyprland.org/Configuring/Dispatchers/",
    "window_rules": "https://wiki.hyprland.org/Configuring/Window-Rules/",
    "monitors": "https://wiki.hyprland.org/Configuring/Monitors/",
}


def fetch_content(url: str) -> str:
    """Fetch content from a URL."""
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return response.read().decode('utf-8')
    except urllib.error.URLError as e:
        return f"Error fetching {url}: {e}"


def search_in_content(content: str, query: str, section_name: str) -> List[str]:
    """Search for a query in the content and return matching sections."""
    results = []
    lines = content.split('\n')
    
    # Search case-insensitively
    query_lower = query.lower()
    
    for i, line in enumerate(lines):
        if query_lower in line.lower():
            # Get context: current line and a few lines after
            context_lines = lines[i:min(i+5, len(lines))]
            result = f"\n[{section_name}] Match found:\n" + '\n'.join(context_lines[:5])
            results.append(result)
    
    return results


def search_all_docs(query: str) -> Dict[str, List[str]]:
    """Search all Hyprland documentation for the query."""
    all_results = {}
    
    for section, url in WIKI_URLS.items():
        print(f"Searching {section}...", file=sys.stderr)
        content = fetch_content(url)
        
        if content.startswith("Error"):
            all_results[section] = [content]
        else:
            matches = search_in_content(content, query, section)
            if matches:
                all_results[section] = matches
    
    return all_results


def list_sections():
    """List all available documentation sections."""
    print("Available Hyprland documentation sections:")
    for section, url in WIKI_URLS.items():
        print(f"  - {section}: {url}")


def main():
    if len(sys.argv) < 2:
        print("Usage: search_hyprland_docs.py <search_query>")
        print("       search_hyprland_docs.py --list  (list all documentation sections)")
        print("\nExample: search_hyprland_docs.py 'general:gaps_in'")
        print("Example: search_hyprland_docs.py 'border_size'")
        sys.exit(1)
    
    if sys.argv[1] == "--list":
        list_sections()
        sys.exit(0)
    
    query = sys.argv[1]
    print(f"Searching Hyprland documentation for: '{query}'", file=sys.stderr)
    print("=" * 60, file=sys.stderr)
    
    results = search_all_docs(query)
    
    if not results:
        print(f"\nNo results found for '{query}'")
        print("\nTip: Try searching for:")
        print("  - Config variable names (e.g., 'gaps_in', 'border_size')")
        print("  - Keywords (e.g., 'monitor', 'bind', 'exec')")
        print("  - Feature names (e.g., 'animations', 'blur')")
        sys.exit(1)
    
    print(f"\nFound {len(results)} section(s) with matches:\n")
    
    for section, matches in results.items():
        print(f"\n{'='*60}")
        print(f"SECTION: {section.upper()}")
        print(f"URL: {WIKI_URLS[section]}")
        print('='*60)
        for match in matches:
            print(match)
            print('-' * 40)
    
    print(f"\n\nSearch complete. Found matches in {len(results)} section(s).")


if __name__ == "__main__":
    main()
