package com.example.delivery;

import org.springframework.web.bind.annotation.*;
import java.util.Map;

@RestController
public class DeliveryController {

    private final DeliveryService service = new DeliveryService();

    @PostMapping("/calculateCost")
    public Map<String, Integer> calculateCost(@RequestBody Map<String, Integer> order) {
        int cost = service.calculateCost(order);
        return Map.of("cost", cost);
    }
}
