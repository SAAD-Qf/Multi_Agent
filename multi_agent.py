from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
import os

load_dotenv()
set_tracing_disabled(True)

provider = AsyncOpenAI(
    api_key = os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client= provider,
)

# Create the agent

general = Agent (
    name = "General Questions",
    instructions="you are expert in answering multiple questions around the world any type of questions.",
    model=model,

)    


frontend = Agent(
    name = "FrontEnd Develpor ",
    instructions= "You are an expert in HTML, CSS, JavaScript, React, Framer-motion , Gsap responsive and modern frontend design.",
    model = model,
)

backend = Agent(
    name = "BackEnd Develpor",
    instructions= "You are a backend expert in Node.js, Python, APIs, and databases.",
    model = model,
)

graphic_designer = Agent(
    name = "Graphic Designer",
    instructions= "You are a creative expert in Adobe tools, Figma, logo design, and brand assets.",
    model = model,
)

Fullstack = Agent(
    name = "Full-Stack Develper ",
    instructions= "You are expert in React , Nextjs , javaScript , Html , Css , Tailwind Css , Node js , Express js , Mango db , Python , Apis and databases",
    model = model,
)

async def new_Agent(user_input):
    manager = Agent(
        name = "Manager",
        instructions= "Decide which agent should be used to handle the task.",
        model = model,
        handoffs= [general,frontend, backend, graphic_designer , Fullstack]
    ) 

    response = await Runner.run(
        manager,
        input = user_input
    )

    return response.final_output

