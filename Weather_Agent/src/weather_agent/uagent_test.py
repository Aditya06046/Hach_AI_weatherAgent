from uagents import Agent, Context

agent = Agent(name="alice")
print("hello from out of main")




@agent.on_interval(period=2.0)
async def say_hello(ctx: Context):
    ctx.logger.info("Hello!")


if __name__ == "__main__":
    agent.run()