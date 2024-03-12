# 💻 My Automation Project 
✅ This project demonstrates API call test automation for a hotel application designed to run via the Command Line Interface (CMD). Unlike traditional websites or mobile applications, this CMD-based application is installed and executed directly on a computer's command line interface.

The project was tested and scored: ⭐⭐⭐⭐⭐

## 📖 Overview

This repository contains a Python project focused on automating API calls within a hotel management application. The project leverages various Python libraries and frameworks to interact with the hotel application's API endpoints, enabling functionalities such as adding, retrieving, updating, and deleting hotels.

## 📑 Technologies & Skill & Features
| Technologies      | Description |
| ----------- | ----------- |
| **Python:**      | Python is a versatile, high-level programming language known for its simplicity and readability. It is used for scripting, automation, and web development, making it ideal for API testing and automation tasks.       |
| **pytest:**   | pytest is a testing framework for Python that makes it easy to write simple and scalable test cases. It provides features such as fixture management, parameterization, and detailed reporting, making it well-suited for API testing.        |
| **requests:**   | The requests library is a popular Python HTTP library for making HTTP requests. It simplifies the process of sending HTTP requests and handling responses, making it ideal for interacting with RESTful APIs.        |
| **Allure:**   | Allure is a flexible test reporting tool that provides detailed and visually appealing reports for test execution results. It supports various programming languages and testing frameworks, enabling comprehensive reporting for API test automation projects.        |
| **Faker:**   | Faker is a Python library that generates fake data for a variety of purposes, including testing and automation. It simplifies the process of creating realistic test data, making it useful for API test case generation.        |
| **Object-Oriented Programming (OOP):**   | OOP is a programming paradigm based on the concept of "objects," which can contain data and code to manipulate that data. It promotes modularity, reusability, and scalability in software development, making it suitable for organizing test cases and utilities in API automation projects.        |
| **HTTP Status Codes:**   | HTTP status codes are standardized codes returned by web servers to indicate the result of a request. Understanding HTTP status codes is essential for API testing, as they provide information about the success or failure of API requests.        |
| **Postman:**   | Postman is a popular API testing tool that simplifies the process of API testing and development. It provides a user-friendly interface for creating and sending HTTP requests, as well as tools for organizing and managing APIs. Postman supports features such as request chaining, automated testing, and collaboration, making it an essential tool for API testing and development.        |
| **Git:**   | Git is a distributed version control system used for tracking changes in software development projects. It facilitates collaboration, code review, and version management, making it essential for managing source code and project files in API automation projects.        |

## 📥 Download

**Download the App:**
- [spring-boot-rest-example-master.zip](https://cdn.fs.teachablecdn.com/JOTIPx1VSeCB1TqJcPTO)

   ## 🚀 Launching the Hotel Application

1. **Unzip the file to a folder:** Ensure JDK is installed as the application supports Java version 8 only.
2. **Install Maven:** Maven must be installed to run the application.
3. **Open CMD:** Open the command prompt.
4. **Navigate to the application folder:** Use the `cd` command to navigate to the folder where the application is deployed.
5. **Run the following command:** Execute the following command in the command prompt:
     ```bash
     mvn spring-boot:run -Drun.arguments="spring.profiles.active=test"
     ```

> ⚠️ **Important:**
> As soon as we close the CMD window, the application will shut down and the memory of the actions we performed in the API will be deleted.


## 📊 Reports
  ```bash
  mvn allure:serve
  ```

## 📊 Reports Examples
<p>
  <img src="https://webdriver.io/assets/images/allure-bb6c9b036b07594235a5aca5aff5ac43.png" width="40%" title="Example for screenshot on reports from allure"  />
  <img src="https://i.stack.imgur.com/zmzcz.png" width="40%" title="Example for screenshot on reports from allure"  />
  <img src="https://i.stack.imgur.com/UGjLe.jpg" width="40%" title="Example for screenshot on reports from allure"  />
  <img src="https://sorokin.engineer/images/allure-report.png" width="40%" title="Example for screenshot on reports from allure"  />
</p>

## 🚀 Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/achiyat/HotelsApp-Auto-Python.git
    ```

## 📁 Project Structure
```
├───.idea
├───tests
│   ├───allure-results
│   ├───delete
│   ├───get
│   ├───post
│   ├───put
│   └───__pycache__
└───venv
```

Thanks for visiting my GitHub profile! 😊
Achiya Tzuriel 
