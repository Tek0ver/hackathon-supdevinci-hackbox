<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use App\Models\Client;
use App\Models\Test;

class Machine extends Model
{
    use HasFactory;
    protected $table = 'machine';

    // Relation entre Machine et Test : Une machine peut avoir plusieurs tests
    public function tests()
    {
        return $this->hasMany(Test::class);
    }

    // Relation entre Machine et Client : Une machine appartient à un client
    public function client()
    {
        return $this->belongsTo(Client::class);
    }
}
