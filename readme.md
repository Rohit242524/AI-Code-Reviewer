# AI Code Reviewer

## Overview

AI Code Reviewer is a prototype web application that uses Google's Gemini API to review Python code and provide intelligent feedback.

Users can paste Python code into the application, submit it for analysis, and receive AI-generated suggestions regarding code quality, readability, best practices, and potential improvements.

This project is built as a learning-focused AI application to understand the fundamentals of LLM integration, prompt engineering, backend API development, and AI-assisted software tooling.

---

## Problem Statement

Developers often spend significant time reviewing code for common issues such as:

* Poor variable naming
* Readability concerns
* Code smells
* Missing documentation
* Inefficient logic
* General best-practice violations

This project explores whether an LLM can automate a portion of the code review process and provide useful feedback instantly.

---

## Objectives

The primary goal of this prototype is to:

* Accept Python code from a user
* Send the code to Gemini API
* Generate AI-based review feedback
* Display structured suggestions to the user

---

## Features

### Current Features

* Python code review
* Gemini API integration
* Structured review output
* FastAPI backend
* Simple web interface

### Review Categories

The AI reviewer can provide feedback on:

* Code readability
* Variable naming
* Function design
* Best practices
* Documentation quality
* Potential bugs
* Improvement suggestions

---

## Functional Requirements

### FR-1

User can paste Python code.

### FR-2

User can submit code for review.

### FR-3

Backend receives code.

### FR-4

Code is sent to Gemini API.

### FR-5

Gemini analyzes the code.

### FR-6

Review feedback is returned.

### FR-7

Review results are displayed.

---

## Non-Functional Requirements

* Simple and lightweight interface
* Local execution support
* Response time under 20 seconds
* No authentication required
* Prototype-focused architecture

---

## Technology Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* FastAPI

### AI Layer

* Gemini API

---

## High-Level Architecture

User → Frontend → FastAPI Backend → Gemini API → FastAPI Backend → Frontend

---

## Future Improvements

* Multi-language support
* GitHub integration
* Authentication
* Review history
* File uploads
* Rule-based static analysis
* Hybrid AI + Static Analysis review system

---

## Project Status

Prototype Development Phase

Current Stage:
Requirement Gathering and System Design
