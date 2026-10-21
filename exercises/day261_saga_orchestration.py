"""Day 261: Saga Orchestrator."""

class SagaOrchestrator:
    def __init__(self):
        self.steps = []
        self.compensations = []

    def add_step(self, action, compensate):
        self.steps.append(action)
        self.compensations.append(compensate)

    def execute(self):
        executed = []
        for i, step in enumerate(self.steps):
            try:
                step()
                executed.append(i)
            except Exception:
                # Run compensations in reverse
                for comp_idx in reversed(executed):
                    self.compensations[comp_idx]()
                return False
        return True

if __name__ == "__main__":
    log = []
    saga = SagaOrchestrator()
    saga.add_step(lambda: log.append("order_created"), lambda: log.append("order_cancelled"))
    saga.add_step(lambda: (_ for _ in ()).throw(ValueError("card_declined")), lambda: log.append("payment_refunded"))
    success = saga.execute()
    assert success is False
    assert "order_cancelled" in log
    print("Day 261 Saga Orchestration tests passed!")
