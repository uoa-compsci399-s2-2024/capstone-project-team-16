# Chatbots as Interactive Storytellers

## Project Management Tool

https://aistoryteller-399.atlassian.net/jira/software/projects/SOUR/boards/2/timeline

## Contributors

- Hadas Livne
- Tasal (Noah) Amad 
- Willow Te Kapaiwaho
- Sam De Suza
- Avery O'Callahan
- Finn Laville-Moore

## Project Description

This capstone project for COMPSCI 399 at the University of Auckland leverages OpenAI's creative capabilities to craft interactive stories. 
The project prompts large language models (LLMs) to generate scenes, choices, storylines, and characters while keeping track of crucial 
story details. The result is a consistent, endlessly evolving interactive narrative where no two playthroughs are the same. It's been developed
in the likeness of a pick-your-path adventure game where each turn you're given a range of choices to chose that progress the story. Our team built
a custom engine from the ground up to interact with OpenAI's GPT-4o-mini model to store and manipulate every aspect of our game thus giving us full access
on how we wanted our stories to be crafted and displayed.

## Project Motivation

Large language models (LLMs), such as ChatGPT, have been rising in popularity globally. With this rise in popularity comes a need to determine the most 
effective way to use these models for various tasks. One such task is storytelling - generative AI seems, at a glance, to be incredibly well-suited for 
generating fictional narratives in ways humans can’t. It can be used to generate a constantly changing, truly interactive pick-a-path story, whereas 
pick-a-paths written by humans only seem as though the reader influences the narrative. However, LLMs stumble into issues when storytelling, chief among 
them their limited memory and ability to keep track of the context and details required to create a coherent narrative. That's where we come in. We wanted
to create a product that would address these shortcomings and demonstrate the power of generative storytelling that when done right could craft truly immersive
immersive narratives consistently. Our team is incredibly passionate about showcasing its potential and bringing further attention to this area which is what 
drove us to pick this project.

## Installation

Note: The current working directory to run the program from should be 1 level above the src folder 
in the capstone-project-team-16 folder. 

 ### Windows:
- $ cd \<project directory>
- $ pip install -r requirements.txt
- $ python src/main.py

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
