"use client";

import Form from "@/components/Form";

export default function Login() {

    return <Form route="/api/auth/login/" method="login" />;
}
