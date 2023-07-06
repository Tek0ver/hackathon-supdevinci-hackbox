<?php

namespace App\Http\Controllers;

use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Routing\Controller as BaseController;
use App\Models\Client;
use App\Models\Machine;
use App\Models\Test;
use Illuminate\Http\Request;

class Controller extends BaseController
{
    use AuthorizesRequests, DispatchesJobs, ValidatesRequests;

    public function index()
    {
        $machines = Machine::all();
        $clients = Client::with('machines.tests')->get();
        $clientId = 0;
        $ip = null;

        return view('welcome', ['clients' => $clients, 'machines' => $machines, 'clientId' => $clientId, 'ip' => $ip]);
    }

    public function handleSearch(Request $request)
    {
        $clientId = $request->input('id');
        $ip = $request->input('ip');

        // Récupérer les clients et appliquer les filtres si nécessaire
        $clients = Client::with('machines.tests')->get();
        $clientasked = null; // Initialiser la variable $clientasked à null

        if ($clientId !== '0') {
            // Filtrer par le client sélectionné
            $clientasked = Client::where('id', $clientId)->get();
            $machines = $clientasked->first()->machines();
        
            if ($ip) {
                $machines = $machines->where('ip', 'LIKE', '%' . $ip . '%')->get();
            } else {
                $machines = $machines->get();
            }
        } else {
            // Aucun client sélectionné, récupérer toutes les machines
            $machines = Machine::query();
        
            if ($ip) {
                $machines = $machines->where('ip', 'LIKE', '%' . $ip . '%')->get();
            } else {
                $machines = $machines->get();
            }
        }

        // Passer les données des clients, machines et tests à la vue
        return view('welcome', compact('clients', 'clientasked', 'machines', 'clientId', 'ip'));
    }
}
