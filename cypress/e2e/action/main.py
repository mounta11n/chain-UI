import chainlit as cl


@cl.action_callback("test action")
async def on_action():
    await cl.Message(content="Executed test action!").send()


@cl.action_callback("removable action")
async def on_action(action: cl.Action):
    await cl.Message(content="Executed removable action!").send()
    await action.remove()


@cl.action_callback("multiple actions")
async def on_action(action: cl.Action):
    await cl.Message(content=f"Action(id={action.id}) has been removed!").send()
    await action.remove()


@cl.on_chat_start
async def main():
    actions = [
        cl.Action(name="test action", value="test"),
        cl.Action(name="removable action", value="test"),
        cl.Action(name="label action", value="test", label="Test Label"),
        cl.Action(
            name="multiple actions",
            value="multiple action one",
            label="multiple action one",
        ),
        cl.Action(
            name="multiple actions",
            value="multiple action two",
            label="multiple action two",
        ),
    ]
    await cl.Message("Hello, this is a test message!", actions=actions).send()
