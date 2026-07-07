import json

from repro_eval.collectors.agent import collector_result_from_agent_payload, parse_agent_response


def test_parse_agent_response_accepts_object_payload():
    payload = {
        "metrics_patch": {"task_metrics": {"P01": {"x": 1}}},
        "rules_evaluated": [
            {
                "rule_id": "R01",
                "evidence_status": "evidence_found",
                "extracted_value": 1,
                "source_file": "results/a.json",
                "mapping_confidence": 0.9,
                "notes": "ok",
            }
        ],
    }
    parsed = parse_agent_response(json.dumps(payload))
    result = collector_result_from_agent_payload(parsed)
    assert result.metrics["task_metrics"]["P01"]["x"] == 1
    assert result.evidence[0].rule_id == "R01"


def test_parse_agent_response_accepts_markdown_fenced_list():
    parsed = parse_agent_response(
        """```json
        [{"rule_id":"R02","evidence_status":"no_evidence","extracted_value":null,"source_file":"","mapping_confidence":0,"notes":"missing"}]
        ```"""
    )
    assert parsed["rules_evaluated"][0]["rule_id"] == "R02"
