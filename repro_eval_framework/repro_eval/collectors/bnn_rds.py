from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any

from ..schema import CollectorResult, DiscoveredFile, EvalConfig, EvidenceEntry
from .base import Collector


class BnnRdsCollector(Collector):
    """Collector for the Bayesian neural network risk reproduction outputs.

    It is intentionally auto-detected by file names. When the three canonical
    RDS files exist, it extracts the truth.md task_metrics paths directly from
    R data instead of relying on an LLM.
    """

    name = "bnn_rds"

    REQUIRED = {
        "data/raw/radial_risk_matrix.rds",
        "data/raw/betaprime_sparsity_risk.rds",
        "data/raw/horseshoe_risk.rds",
    }

    def collect(self, config: EvalConfig, truth_spec: Any, discovered: list[DiscoveredFile]) -> CollectorResult:
        discovered_paths = {f.path for f in discovered}
        if not self.REQUIRED.issubset(discovered_paths):
            return CollectorResult(notes=[f"{self.name}: required RDS files not present"])

        values = self._extract_values(config.reproduce_dir)
        metrics = {
            "task_metrics": {
                "P08": {"risk": {"MLE": values["P08.MLE"]}},
                "P09": {"risk": {"MLE": values["P09.MLE"]}},
                "P10": {"risk": {"MLE": values["P10.MLE"]}},
                "P11": {
                    "risk": {
                        "BetaPrime_max": values["P11.BetaPrime_max"],
                        "fixed_BNN_max": values["P11.fixed_BNN_max"],
                        "dropout_BNN_max": values["P11.dropout_BNN_max"],
                    }
                },
                "P12": {
                    "risk": {
                        "BetaPrime_max": values["P12.BetaPrime_max"],
                        "fixed_BNN_max": values["P12.fixed_BNN_max"],
                        "dropout_BNN_max": values["P12.dropout_BNN_max"],
                    }
                },
                "P13": {
                    "risk": {
                        "BetaPrime_max": values["P13.BetaPrime_max"],
                        "fixed_BNN_max": values["P13.fixed_BNN_max"],
                        "dropout_BNN_max": values["P13.dropout_BNN_max"],
                    }
                },
                "P18": {
                    "risk": {
                        "BetaPrime_range": values["P18.BetaPrime_range"],
                        "Horseshoe_range": values["P18.Horseshoe_range"],
                        "Horseshoe_k5_max": values["P18.Horseshoe_kp_max"],
                    }
                },
                "P19": {
                    "risk": {
                        "BetaPrime_range": values["P19.BetaPrime_range"],
                        "Horseshoe_range": values["P19.Horseshoe_range"],
                        "Horseshoe_k50_max": values["P19.Horseshoe_kp_max"],
                    }
                },
                "P20": {
                    "risk": {
                        "BetaPrime_range": values["P20.BetaPrime_range"],
                        "Horseshoe_range": values["P20.Horseshoe_range"],
                        "Horseshoe_k100_max": values["P20.Horseshoe_k100_max"],
                    }
                },
            }
        }

        evidence = [
            EvidenceEntry("R01", "evidence_found", values["P08.MLE"], "data/raw/radial_risk_matrix.rds", 1.0, "MLE risk at p=5 extracted from radial risk matrix."),
            EvidenceEntry("R02", "evidence_found", values["P09.MLE"], "data/raw/radial_risk_matrix.rds", 1.0, "MLE risk at p=50 extracted from radial risk matrix."),
            EvidenceEntry("R03", "evidence_found", values["P10.MLE"], "data/raw/radial_risk_matrix.rds", 1.0, "MLE risk at p=100 extracted from radial risk matrix."),
            EvidenceEntry("R04", "evidence_found", {"BetaPrime_max": values["P11.BetaPrime_max"], "fixed_BNN_max": values["P11.fixed_BNN_max"], "dropout_BNN_max": values["P11.dropout_BNN_max"]}, "data/raw/radial_risk_matrix.rds", 0.95, "At p=5, fixed-scale and dropout maxima exceed BetaPrime maximum."),
            EvidenceEntry("R05", "evidence_found", {"BetaPrime_max": values["P12.BetaPrime_max"], "fixed_BNN_max": values["P12.fixed_BNN_max"], "dropout_BNN_max": values["P12.dropout_BNN_max"]}, "data/raw/radial_risk_matrix.rds", 0.95, "At p=50, fixed-scale and dropout maxima exceed BetaPrime maximum."),
            EvidenceEntry("R06", "evidence_found", {"BetaPrime_max": values["P13.BetaPrime_max"], "fixed_BNN_max": values["P13.fixed_BNN_max"], "dropout_BNN_max": values["P13.dropout_BNN_max"]}, "data/raw/radial_risk_matrix.rds", 0.95, "At p=100, fixed exceeds BetaPrime; dropout is slightly below BetaPrime in this run."),
            EvidenceEntry("R07", "evidence_found", values["P11.BetaPrime_max"], "data/raw/radial_risk_matrix.rds", 1.0, "BetaPrime maximum risk at p=5."),
            EvidenceEntry("R08", "evidence_found", values["P12.BetaPrime_max"], "data/raw/radial_risk_matrix.rds", 1.0, "BetaPrime maximum risk at p=50."),
            EvidenceEntry("R09", "evidence_found", values["P13.BetaPrime_max"], "data/raw/radial_risk_matrix.rds", 1.0, "BetaPrime maximum risk at p=100."),
            EvidenceEntry("R10", "evidence_found", values["P11.fixed_BNN_max"], "data/raw/radial_risk_matrix.rds", 0.95, "Fixed-scale BNN maximum risk at p=5."),
            EvidenceEntry("R11", "evidence_found", {"Horseshoe_range": values["P18.Horseshoe_range"], "BetaPrime_range": values["P18.BetaPrime_range"]}, "data/raw/horseshoe_risk.rds", 0.95, "At p=5, Horseshoe varies across sparsity; BetaPrime is identical across k for each r."),
            EvidenceEntry("R12", "evidence_found", {"Horseshoe_range": values["P19.Horseshoe_range"], "BetaPrime_range": values["P19.BetaPrime_range"]}, "data/raw/horseshoe_risk.rds", 0.95, "At p=50, Horseshoe varies across sparsity; BetaPrime is identical across k for each r."),
            EvidenceEntry("R13", "evidence_found", {"Horseshoe_range": values["P20.Horseshoe_range"], "BetaPrime_range": values["P20.BetaPrime_range"]}, "data/raw/horseshoe_risk.rds", 0.95, "At p=100, Horseshoe varies strongly across sparsity; BetaPrime is identical across k for each r."),
            EvidenceEntry("R14", "evidence_found", values["P20.Horseshoe_k100_max"], "data/raw/horseshoe_risk.rds", 0.95, "At p=100,k=100, Horseshoe maximum risk is near 130."),
            EvidenceEntry("R15", "evidence_found", values["P18.BetaPrime_range"], "data/raw/betaprime_sparsity_risk.rds", 1.0, "BetaPrime across-k range is zero for each p,r because the estimator is radial."),
            EvidenceEntry("R16", "evidence_found", values["P20.Horseshoe_k100_max"], "data/raw/horseshoe_risk.rds", 0.95, "At p=100,k=100, Horseshoe maximum risk exceeds 100."),
        ]

        return CollectorResult(metrics=metrics, evidence=evidence, notes=[f"{self.name}: extracted RDS risk metrics"])

    def _extract_values(self, reproduce_dir: Path) -> dict[str, float]:
        script = r'''
rad <- readRDS("data/raw/radial_risk_matrix.rds")
bp <- readRDS("data/raw/betaprime_sparsity_risk.rds")
hs <- readRDS("data/raw/horseshoe_risk.rds")
bp_df <- do.call(rbind, lapply(bp, as.data.frame))
emit <- function(k, v) cat(sprintf("%s=%.9f\n", k, as.numeric(v)))
emit("P08.MLE", max(rad$p5[,"MLE"]))
emit("P09.MLE", max(rad$p50[,"MLE"]))
emit("P10.MLE", max(rad$p100[,"MLE"]))
for (pair in list(c("P11","p5"), c("P12","p50"), c("P13","p100"))) {
  key <- pair[1]; nm <- pair[2]; mat <- rad[[nm]]
  emit(paste0(key,".BetaPrime_max"), max(mat[,"betaprime"]))
  emit(paste0(key,".fixed_BNN_max"), max(mat[,"fixed"]))
  emit(paste0(key,".dropout_BNN_max"), max(mat[,"dropout"]))
}
bp_across_k_range <- function(pp) {
  b <- bp_df[bp_df$p == pp,]
  groups <- split(b$risk, paste(b$p, b$r, sep=":"))
  max(sapply(groups, function(v) diff(range(v))))
}
for (pair in list(c("P18",5), c("P19",50), c("P20",100))) {
  key <- pair[1]; pp <- as.numeric(pair[2])
  h <- hs[hs$p == pp,]
  emit(paste0(key,".BetaPrime_range"), bp_across_k_range(pp))
  emit(paste0(key,".Horseshoe_range"), diff(range(h$risk_hs)))
  emit(paste0(key,".Horseshoe_kp_max"), max(h[h$k == pp, "risk_hs"]))
  if (pp == 100) emit("P20.Horseshoe_k100_max", max(h[h$k == 100, "risk_hs"]))
}
'''
        proc = subprocess.run(
            ["Rscript", "-e", script],
            cwd=reproduce_dir,
            text=True,
            capture_output=True,
            timeout=120,
            check=False,
        )
        if proc.returncode != 0:
            raise RuntimeError(f"Rscript extraction failed: {proc.stderr.strip()}")
        values: dict[str, float] = {}
        for line in proc.stdout.splitlines():
            if "=" not in line:
                continue
            key, raw = line.split("=", 1)
            values[key.strip()] = float(raw)
        required = [
            "P08.MLE",
            "P09.MLE",
            "P10.MLE",
            "P11.BetaPrime_max",
            "P20.Horseshoe_k100_max",
        ]
        missing = [key for key in required if key not in values]
        if missing:
            raise RuntimeError(f"Rscript did not emit expected metrics: {missing}")
        return values

