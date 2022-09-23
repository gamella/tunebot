import asyncio
from typing import List

import streamlit as st
import schedule
import time

DATA = []

async def job():
    print("I'm working...")
    DATA.append(1)

async def main():

    schedule.every(1).minutes.do(job)

    st.markdown("# Trade")
    element = st.empty()

    while True:
        element.dataframe(DATA)
        time.sleep(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
