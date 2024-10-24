# Chatbots as Interactive Storytellers

## Project management tool

https://aistoryteller-399.atlassian.net/jira/software/projects/SOUR/boards/2/timeline

## Contributors

- Hadas Livne
- Tasal (Noah) Amad 
- Willow Te Kapaiwaho
- Sam De Suza
- Avery O'Callahan
- Finn Laville-Moore

## Project Description

This capstone project for COMPSCI 399 at the University of Auckland leverages OpenAI's creative capabilities to craft interactive stories. The project prompts large language models (LLMs) to generate scenes, choices, storylines, and characters while keeping track of crucial story details. The result is a consistent, endlessly evolving interactive narrative where no two playthroughs are the same.

## Motivation

The advent of LLMs has opened up new avenues for creating unique and engaging stories. By using these models, we can generate content that surpasses the limits of traditional human storytelling. However, while popular LLMs excel at generating ideas, they often lack the consistency required to be effective storytellers on their own. Our project addresses this by delegating the task of maintaining narrative coherence to our software, ensuring a seamless and cohesive story experience.

We aim to deliver an authentic storytelling experience, emphasizing consistency and narrative cohesion. Additionally, our project explores innovative approaches to integrating LLMs with our software at a granular level. Currently, we prompt OpenAI to return much of its story data in JSON format, allowing for greater control and flexibility in story creation.

## Installation

To install the project requirements, run:

```pip install -r requirements.txt```

To start the program, simply execute:

```python main.py```

## Technologies Used

- Python 3.11 or newer
- OpenAI's GPT-4o-mini model
- PyLint 
- PyTest 8.3.2 
- Python-Dotenv 1.0.1
- OpenAI API 1.41.0
- Pandas 2.2.2
- NetworkX 3.3.0
- Matplotlib 3.9.2
- Pydantic 2.8.2

## Current Features

- A playable choose your own adventure style game
- A game engine that keeps track of all game elements (locations, items, characters, tropes, world-state, etc.)
- LLM generated story scenes that forma cohesive and sensible plot
- LLM generated sensible options for the user to choose from
- LLM generated new game elements which are added to the engine
- Multiple possible action types (move location, interact with item, pick up item, put down item, use item, talk to character)
- Novel storytelling through the incorporation of randomised tropes (plot, protagonist and antagonist) and themes
- Incorporation of a clear story arc in each playthrough through the incorporation of story beats and an algorithm to randomise beat intervals with an increasing probability of moving beat
- Graphical representation of locations with edges between connected locations
- Game playthrough saving

## Future Plan

- Construct story arcs more intelligently
- Increase the variety of actions (e.g. add combat actions)
- Have variable amounts of user choices
- Support asynchronous calls to ChatGPT
- Create a front-end that improves interaction with game features (e.g. saving, viewing a map, AI generated pictorial scene representations, etc.)
- Implement autonomous agent interactions beyond the player’s view
- Create technical documentation and tools for researchers
