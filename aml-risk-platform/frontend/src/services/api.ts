import keycloak from "./keycloak";

const API_URL = "http://localhost:8000";

export async function getCurrentUser() {
    if (!keycloak.token) {
        throw new Error("Not authenticated");
    }

    await keycloak.updateToken(30);

    const response = await fetch(
        `${API_URL}/api/v1/auth/me`,
        {
            method: "GET",
            headers: {
                Authorization: `Bearer ${keycloak.token}`,
                "Content-Type": "application/json",
            },
        },
    );

    if (!response.ok) {
        throw new Error(
            `API request failed: ${response.status}`,
        );
    }

    return response.json();
}