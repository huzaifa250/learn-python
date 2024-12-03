import asyncio


# Define an asynchronous function
async def say_hello():
    print("Hello!")
    await asyncio.sleep(1)  # Simulates a delay (non-blocking)
    print("World!")


# Main async function to coordinate tasks
async def main():
    print("Start")
    await say_hello()  # Await the async function
    print("End")


# Execute the async program using asyncio.run()
asyncio.run(main())
