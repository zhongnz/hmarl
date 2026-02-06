# Hierarchical Multi-Agent Reinforcement Learning for Congestion-Aware Vessel Scheduling with Predictive Port Coordination

**Supervised by Prof. Aboussalah**  
**Spring 2026 Independent Study**

## 1. Introduction and Motivation

Maritime logistics accounts for approximately 80% of global trade volume, yet operational inefficiencies, particularly port congestion, result in significant fuel waste, emissions, and delays. Port waiting times can account for 5–15% of total trip duration, with vessels burning fuel while standing by. Effective maritime logistics requires coordination between multiple stakeholders: vessels making routing and speed decisions, and ports managing dock allocation and service scheduling.

Recent work on constrained hierarchical multi-agent reinforcement learning (CH-MARL) demonstrates that decomposing maritime operations into cooperating agents at different hierarchical levels captures realistic decision-making structures. However, these approaches typically assume stationary environments. In practice, port congestion is often driven by non-stationary factors, including weather disruptions, fluctuating demand, and unexpected delays.

Integrating predictive models of port congestion into multi-agent coordination frameworks can enable more proactive and adaptive scheduling, allowing both vessel and port agents to anticipate future bottlenecks rather than merely react.

## 2. Problem Statement and Research Gap

### Problem

A maritime logistics system involves multiple vessels navigating among several ports, each managed by a port agent. A Fleet Coordinator agent oversees the fleet, making strategic decisions such as selecting destination ports, setting departure windows, and allocating emission budgets.

- Vessel agents decide on routing and speed to execute strategic plans.
- Port agents allocate docks and schedule services.
- All agents coordinate to minimize system costs (fuel, delays, emissions) while accounting for predicted congestion.

### Research Gap

Current maritime MARL research generally follows one of two paths:

1. Vessel-to-vessel competition without proactive congestion forecasting.
2. Port-aware settings where ports are passive environment components, not active decision-makers.

The integration of learned congestion forecasts with cooperative fleet, vessel, and active port agents remains underexplored.

### Scope

To maintain feasibility within four months, the system includes:

- 1 Fleet Coordinator
- 8 Vessel agents
- 5 Port agents

## 3. Research Questions

1. How can heterogeneous agents (vessels, ports, fleet coordinator) coordinate using shared congestion forecasts to minimize delays, fuel, and emissions?
2. How much does proactive predictive coordination improve performance versus:
   - independent policies
   - reactive coordination without forecasting?
3. How should forecast information be distributed among vessel and port agents, and which horizons are most useful?
4. How does improved congestion coordination affect economic outcomes, including transport price and reliability?

## 4. Methodology

### 4.1 Hierarchical Multi-Agent Architecture

Three agent types operate at different timescales:

- **Fleet Coordinator (12–24h):** strategic routing, departure windows, emission budgets.
- **Vessels (1–4h):** speed control and arrival slot requests.
- **Ports (2–6h):** dock allocation and service queue prioritization.

Forecasting is shared across layers to support proactive coordination.

```text
Fleet Coordinator  -> (Strategic Directives) -> Vessel Agents -> (Arrival Requests) -> Port Agents
Port Agents        -> (Dock Availability)    -> Vessel Agents
```

### 4.2 MDP Formulation

Each agent type is modeled as an MDP: ⟨S, A, P, R, γ⟩.

#### Fleet Coordinator MDP

- **State:** medium-term forecasts (3–7 days), vessel states, cumulative emissions.
- **Action:** destination port, departure window, emission budget.
- **Reward:** negative expected voyage cost + emission penalty.

#### Vessel MDP

- **State:** short-term forecasts (6–24h), vessel state, coordinator directives, port availability.
- **Action:** speed and requested arrival time.
- **Reward:** negative weighted fuel, delay, and emissions.

#### Port MDP

- **State:** queue lengths, dock occupancy, predicted arrivals, service completion times.
- **Action:** dock assignment and service priority.
- **Reward:** negative queue delay + dock idle time.

### 4.3 Forecasting Module

Two-tier forecasting:

- **Medium-term (3–7 days, coordinator):** strategic congestion outlook.
- **Short-term (6–24 hours, vessels/ports):** operational congestion and arrival forecasts.

Model families to compare include RNN-based, econometric, and hybrid approaches.

### 4.4 RL Algorithm and Coordination

Use **MAPPO** under centralized training with decentralized execution (CTDE):

1. Coordinator sets strategic directives.
2. Vessels optimize operational actions from directives + forecasts.
3. Vessels request arrival slots from ports.
4. Ports allocate docks using requests + short-term forecasts.
5. Centralized critic evaluates joint outcomes during training.
6. PPO updates all policies.
7. Decentralized policies are used at test/deployment time.

Baselines:

- Independent agents
- Reactive coordinated MARL (no forecasts)
- Oracle with perfect future congestion
- Rule-based heuristics

## 5. Expected Contributions

1. **Methodological:** practical hierarchical MARL with predictive coordination.
2. **Empirical:** quantified gains in delay/fuel/emission/system-cost performance.
3. **Practical:** design guidance for forecast sharing and vessel-port coordination.
4. **Economic:** effects on shipping reliability, variability, and effective transport pricing.

## 6. Experimental Plan and Data

### 6.1 Simulation Environment

Python discrete-event simulation with Gymnasium interfaces for MARL training and evaluation.

### 6.2 Data Sources

- Synthetic data calibrated to realistic literature-based statistics.
- AIS data from major ports (e.g., Singapore, Rotterdam) for fidelity checks.
- Alternative data: text/news signals and satellite-derived congestion indicators.

### 6.3 Evaluation Metrics

- **Forecasting:** MAE, RMSE.
- **System-level:** total cost, average trip duration.
- **Vessel-level:** fuel/trip, on-time arrival.
- **Port-level:** queue length, dock utilization, waiting time.
- **Coordinator-level:** emission compliance, route efficiency.
- **Coordination-level:** request overhead, policy agreement rate.

Ablations:

- Forecast horizon/accuracy
- Coordination style (independent vs coordinated)
- Forecast-sharing schemes
- CTDE variants

## 7. Timeline (4 Months)

- **Month 1 (Feb):** literature review, simulator implementation, heuristic baselines.
- **Month 2 (Mar):** forecasting model implementation and validation, independent baselines.
- **Month 3 (Apr):** MAPPO/CTDE implementation, reactive vs predictive training.
- **Month 4 (May):** ablations, baseline comparisons, final report and presentation.

Weekly checkpoints during VIP office hours.

## 8. Conclusion

This project proposes a hierarchical, forecast-informed MARL framework for congestion-aware maritime scheduling with active port coordination. By combining strategic and operational decision layers with predictive congestion signals, the framework targets lower delays, lower fuel burn, reduced emissions, and improved economic reliability in maritime logistics.

## References

1. Smith, T., Jalkanen, J. P., Anderson, B., et al. (2014). *Third IMO GHG Study 2014*. International Maritime Organization.
2. Alqithami, S. (2025). *CH-MARL: Constrained Hierarchical Multiagent Reinforcement Learning for Sustainable Maritime Logistics*. arXiv:2502.02060.
3. Yu, C., Velu, A., Vinitsky, E., Gao, J., Wang, Y., Bayen, A., & Wu, Y. (2022). *The Surprising Effectiveness of PPO in Cooperative, Multi-Agent Games*. arXiv:2103.01955.
