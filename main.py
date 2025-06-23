from multi_agent import new_Agent
import chainlit as cl
import asyncio

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content="Welcome to Saad's Ai Agents How Can I Help You Today ? There is Multiple Agents To Help You !!! "
    ).send()


@cl.on_message
async def main(message: cl.Message):
    user_input = message.content
    response = asyncio.run(new_Agent(user_input))
    await cl.Message(content= f"{response}"
    ).send()