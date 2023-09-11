import asyncio

import streamlit as st


async def tick(placeholder):
    tick_ = 0
    while True:
        with placeholder:
            tick_ += 1
            st.write(tick_)
            if tick_ == 10:
                break
        await asyncio.sleep(1)


async def tick2(placeholder2):
    tick_ = 0
    while True:
        with placeholder2:
            tick_ += 1
            st.write(tick_)
        await asyncio.sleep(2)


async def main():
    st.header("Async")
    placeholder = st.empty()
    placeholder2 = st.empty()
    await tick(placeholder)
    await tick2(placeholder2)


asyncio.run(main())