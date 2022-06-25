from datetime import datetime
from typing import List

from fastapi import FastAPI, Request, Response, status

from models.get_all_checkins import GetAllCheckinsBody
from models.post_checkin import CheckinBody
from models.constants import BOAT_NAMES
from sql_manager import SqlManager

app = FastAPI()


class Api:
    sql_manager: SqlManager

    def __init__(self):
        self.sql_manager = SqlManager()
        self.sql_manager.initialize()
        print("Initialized app.")

        @app.get("/is-boat-checked-in")
        def is_checked_in(boatname: str):
            return self.handle_is_boat_checked_in(boat_name=boatname)

        @app.post("/checkins")
        def get_checkins(body: GetAllCheckinsBody, response: Response):
            return self.handle_get_checkins(body=body, response=response)

        @app.post("/check-in-or-out/{boat_name}")
        def check_in_or_out(boat_name: str, body: CheckinBody, response: Response):
            return self.handle_check_in_or_out(boat_name=boat_name, body=body, response=response)

    def handle_get_checkins(self, body: GetAllCheckinsBody, response: Response):
        # checkins = {}
        # checkins = ["boat_name,trainer_name,begin,end,comment,amount_refueled"]
        result = {
            "columns": ["boat_name", "trainer_name", "begin", "end", "comment", "amount_refueled"],
            "checkins": []
        }

        for boat_name in BOAT_NAMES:
            boat_checkins = self.sql_manager.get_all_entries_for_boat(boat_name=boat_name)

            for checkin in boat_checkins:
                checkin_data = [
                    boat_name,
                    checkin[1],
                    checkin[2].strftime("%Y-%m-%d %H:%M:%S"),
                    checkin[3].strftime("%Y-%m-%d %H:%M:%S"),
                    checkin[4] if checkin[4] != "None" else "",
                    str(checkin[5]),
                ]

                result["checkins"].append(checkin_data)

        return result

    def handle_check_in_or_out(self, boat_name: str, body: CheckinBody, response: Response):
        action: str
        if boat_name not in BOAT_NAMES:
            response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
            return {
                "success": False,
                "message": f"Bootname '{boat_name}' nicht in Bootsliste"
            }

        if self.sql_manager.is_trainer_currently_checked_in(boat_name=boat_name, trainer_name=body.trainer_name):
            action = "check-out"
            self.sql_manager.check_out(boat_name=boat_name, trainer_name=body.trainer_name)
        else:
            action = "check-in"
            self.sql_manager.check_in(boat_name=boat_name, trainer_name=body.trainer_name, comment=body.comment,
                                      amount_refueled=body.amount_refueled)

        return {"success": True, "action": action}

    def handle_is_boat_checked_in(self, boat_name: str):
        result = self.sql_manager.is_boat_currently_checked_in(boat_name=boat_name)

        return {"isBoatCheckedIn": result}


Api()
