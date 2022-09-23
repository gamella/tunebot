import asyncio
from typing import List

import streamlit as st
import schedule
import time

TRADE_DATA1 = []
TRADE_DATA2 = []

async def main():

    def job1():
        TRADE_DATA1.append(1)

    def job2():
        TRADE_DATA2.append(1)

    schedule.every(5).seconds.do(job1)
    schedule.every(30).seconds.do(job2)

    st.markdown("# Trade1")
    element1 = st.empty()

    st.markdown("# Trade2")
    element2 = st.empty()

    while True:
        schedule.run_pending()
        element1.dataframe(TRADE_DATA1)
        element2.dataframe(TRADE_DATA2)
        time.sleep(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
