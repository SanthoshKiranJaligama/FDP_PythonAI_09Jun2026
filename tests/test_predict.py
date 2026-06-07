import os
# pyrefly: ignore [missing-import]
import pytest
from app.predict import calculate_risk

def test_safe_case():
    # Test case where student is expected to be safe
    # e.g., high scores: Attendance=90, Internal=85, Assignment=80
    # Score should be: (90*0.3 + 85*0.4 + 80*0.3) = 27 + 34 + 24 = 85 / 100 = 0.85
    # For threshold=0.5 (DEV) or 0.7 (TEST), 0.85 should be 'safe'
    result = calculate_risk(90.0, 85.0, 80.0, 0.5)
    assert result["label"] == "safe"
    assert 0.0 <= result["score"] <= 1.0

def test_at_risk_case():
    # Test case where student is expected to be at risk
    # e.g., low scores: Attendance=40, Internal=30, Assignment=50
    # Score should be: (40*0.3 + 30*0.4 + 50*0.3) = 12 + 12 + 15 = 39 / 100 = 0.39
    # For threshold=0.5, 0.39 should be 'at_risk'
    result = calculate_risk(40.0, 30.0, 50.0, 0.5)
    assert result["label"] == "at_risk"
    assert 0.0 <= result["score"] <= 1.0

def test_score_range():
    # Verify score is always between 0 and 1 for extreme inputs
    res_min = calculate_risk(0.0, 0.0, 0.0, 0.5)
    assert res_min["score"] == 0.0
    
    res_max = calculate_risk(100.0, 100.0, 100.0, 0.5)
    assert res_max["score"] == 1.0

def test_exact_example():
    # When inputs are 62, 58, 70, the normalized score is 0.628
    # DEV threshold 0.5 -> safe
    res_dev = calculate_risk(62.0, 58.0, 70.0, 0.5)
    assert res_dev["score"] == 0.628
    assert res_dev["label"] == "safe"

    # TEST threshold 0.7 -> at_risk
    res_test = calculate_risk(62.0, 58.0, 70.0, 0.7)
    assert res_test["score"] == 0.628
    assert res_test["label"] == "at_risk"

def test_main_dev_defaults(monkeypatch):
    # If APP_ENV is dev, default threshold should be 0.5
    monkeypatch.setenv("APP_ENV", "dev")
    monkeypatch.delenv("MODEL_THRESHOLD", raising=False)
    # Mock sys.argv to ensure no CLI arguments override inputs
    monkeypatch.setattr("sys.argv", ["predict.py"])
    from app.predict import main
    result = main()
    assert result["environment"] == "dev"
    assert result["threshold"] == 0.5
    assert result["label"] == "safe"

def test_main_test_defaults(monkeypatch):
    # If APP_ENV is test, default threshold should be 0.7
    monkeypatch.setenv("APP_ENV", "test")
    monkeypatch.delenv("MODEL_THRESHOLD", raising=False)
    monkeypatch.setattr("sys.argv", ["predict.py"])
    from app.predict import main
    result = main()
    assert result["environment"] == "test"
    assert result["threshold"] == 0.7
    assert result["label"] == "at_risk"

def test_main_override(monkeypatch):
    # Verify manual environment override takes precedence
    monkeypatch.setenv("APP_ENV", "test")
    monkeypatch.setenv("MODEL_THRESHOLD", "0.8")
    monkeypatch.setattr("sys.argv", ["predict.py"])
    from app.predict import main
    result = main()
    assert result["environment"] == "test"
    assert result["threshold"] == 0.8

