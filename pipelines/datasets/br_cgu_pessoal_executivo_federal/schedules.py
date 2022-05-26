# -*- coding: utf-8 -*-
"""
Schedules for br_cgu_terceirizados
"""
from datetime import datetime

from prefect.schedules import Schedule, filters, adjustments
from prefect.schedules.clocks import CronClock
from pipelines.constants import constants


every_four_months = Schedule(
    clocks=[
        CronClock(
            cron="0 0 28 2/4 *",
            start_date=datetime(2021, 1, 1, 10, 12),
            labels=[constants.BASEDOSDADOS_DEV_AGENT_LABEL.value],
            filters=[filters.is_weekday],
            adjustments=[adjustments.next_weekday],
            parameter_defaults={
                "dataset_id": "br_cgu_pessoal_executivo_federal",
                "materialization_mode": "dev",
                "materialize after dump": True,
                "table_id": "terceirizados",
            },
        )
    ]
)
