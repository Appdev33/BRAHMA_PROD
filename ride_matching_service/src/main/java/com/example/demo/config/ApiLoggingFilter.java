package com.example.demo.config;

import org.slf4j.MDC;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

@Component
public class ApiLoggingFilter extends OncePerRequestFilter {

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
            throws ServletException, IOException {
        try {
            // Capture request details in MDC
            MDC.put("method", request.getMethod());
            MDC.put("uri", request.getRequestURI());

            // Continue with the request processing
            filterChain.doFilter(request, response);

            // Capture response status in MDC after the response is processed
            MDC.put("status", String.valueOf(response.getStatus()));
        } finally {
            // Clear MDC to prevent data leakage
            MDC.clear();
        }
    }
}
