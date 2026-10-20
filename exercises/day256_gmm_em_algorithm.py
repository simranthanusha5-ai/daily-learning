"""Day 256: 1D Gaussian Mixture Model."""
import math

def normal_pdf(x, mu, sigma):
    sigma = max(sigma, 1e-4)
    return (1.0 / (math.sqrt(2 * math.pi) * sigma)) * math.exp(-0.5 * ((x - mu) / sigma)**2)

def em_gmm_1d_step(data, mu1, sigma1, mu2, sigma2):
    # E-step
    resp1 = []
    resp2 = []
    for x in data:
        p1 = normal_pdf(x, mu1, sigma1)
        p2 = normal_pdf(x, mu2, sigma2)
        total = p1 + p2 + 1e-12
        resp1.append(p1 / total)
        resp2.append(p2 / total)
    # M-step
    new_mu1 = sum(r * x for r, x in zip(resp1, data)) / sum(resp1)
    new_mu2 = sum(r * x for r, x in zip(resp2, data)) / sum(resp2)
    return new_mu1, new_mu2

if __name__ == "__main__":
    data = [1.0, 1.2, 5.0, 5.2]
    mu1, mu2 = em_gmm_1d_step(data, 1.0, 1.0, 5.0, 1.0)
    assert abs(mu1 - 1.1) < 0.1
    assert abs(mu2 - 5.1) < 0.1
    print("Day 256 GMM EM tests passed!")
